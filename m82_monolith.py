#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M82 Sovereign Core – Monolith
Orquestador maestro del sistema M82.
"""

import os
import sys
import time
import signal
import logging
import threading
import queue
from datetime import datetime, timezone  # Añadido timezone
from typing import Dict, Any, Optional
import json

# -------------------------------------------------------------------------
#  Paths y configuración básica
# -------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
LOG_DIR = os.path.join(BASE_DIR, "logs")

DEFAULT_CONFIG_FILE = os.path.join(CONFIG_DIR, "m82_config.json")
RUNTIME_STATE_FILE = os.path.join(CONFIG_DIR, "m82_runtime_state.json")

os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# -------------------------------------------------------------------------
#  Logging
# -------------------------------------------------------------------------

def setup_logging(level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger("M82_MONOLITH")
    logger.setLevel(level)
    logger.propagate = False

    if logger.handlers:
        for h in list(logger.handlers):
            logger.removeHandler(h)

    # Actualizado a datetime.now(timezone.utc)
    log_file = os.path.join(
        LOG_DIR,
        f"m82_monolith_{datetime.now(timezone.utc).strftime('%Y%m%d')}.log"
    )

    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(threadName)s | %(name)s | %(message)s"
    )

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(fmt)
    fh.setLevel(level)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    sh.setLevel(level)

    logger.addHandler(fh)
    logger.addHandler(sh)

    logger.info("Logging inicializado.")
    logger.info("Log file: %s", log_file)
    return logger


LOGGER = setup_logging()

# -------------------------------------------------------------------------
#  Carga de configuración
# -------------------------------------------------------------------------

def load_json_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        LOGGER.warning("Archivo de configuración no encontrado: %s", path)
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        LOGGER.info("Configuración cargada: %s", path)
        return data
    except Exception as e:
        LOGGER.exception("Error cargando configuración %s: %s", path, e)
        return {}


def load_global_config() -> Dict[str, Any]:
    cfg = load_json_config(DEFAULT_CONFIG_FILE)

    env_overrides = {
        "M82_ENV": os.getenv("M82_ENV"),
        "M82_MODE": os.getenv("M82_MODE"),
    }
    cfg.setdefault("env", {})
    for k, v in env_overrides.items():
        if v is not None:
            cfg["env"][k] = v

    LOGGER.info("Config global efectiva: %s", cfg.get("env", {}))
    return cfg


GLOBAL_CONFIG: Dict[str, Any] = load_global_config()

# -------------------------------------------------------------------------
#  Señales de apagado y estado
# -------------------------------------------------------------------------

class ShutdownSignal:
    def __init__(self) -> None:
        self._flag = False
        self._lock = threading.Lock()

    def trigger(self) -> None:
        with self._lock:
            self._flag = True

    def is_triggered(self) -> bool:
        with self._lock:
            return self._flag


SHUTDOWN = ShutdownSignal()


def _handle_signal(sig_num, frame) -> None:
    LOGGER.warning("Recibida señal %s, iniciando apagado ordenado...", sig_num)
    SHUTDOWN.trigger()


signal.signal(signal.SIGINT, _handle_signal)
signal.signal(signal.SIGTERM, _handle_signal)

# -------------------------------------------------------------------------
#  Bus interno de eventos
# -------------------------------------------------------------------------

class EventBus:
    def __init__(self) -> None:
        self._queue: "queue.Queue[Dict[str, Any]]" = queue.Queue()

    def publish(self, event_type: str, payload: Dict[str, Any]) -> None:
        event = {
            "type": event_type,
            "payload": payload,
            "ts": datetime.now(timezone.utc).isoformat()  # Actualizado
        }
        self._queue.put(event)

    def get(self, timeout: Optional[float] = None) -> Optional[Dict[str, Any]]:
        try:
            return self._queue.get(timeout=timeout)
        except queue.Empty:
            return None


EVENT_BUS = EventBus()

# -------------------------------------------------------------------------
#  Stubs para servicios principales
# -------------------------------------------------------------------------

class SentinelManager:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def start(self) -> None:
        LOGGER.info("[Sentinels] Inicializando sentinels con config: %s", self.config)

    def tick(self) -> None:
        LOGGER.debug("[Sentinels] tick()")


class QuantumLedger:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def start(self) -> None:
        LOGGER.info("[Ledger] Inicializando ledger con config: %s", self.config)

    def record_snapshot(self, context: Dict[str, Any]) -> None:
        LOGGER.debug("[Ledger] Registrando snapshot: %s", context)


class WatchlistCore:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def start(self) -> None:
        LOGGER.info("[Watchlist] Inicializando watchlists con config: %s", self.config)

    def refresh(self) -> None:
        LOGGER.debug("[Watchlist] refresh()")

# -------------------------------------------------------------------------
#  Contexto de ejecución
# -------------------------------------------------------------------------

class M82Context:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.env = config.get("env", {})
        self.state: Dict[str, Any] = {}
        self.ledger = QuantumLedger(config.get("ledger", {}))
        self.sentinels = SentinelManager(config.get("sentinels", {}))
        self.watchlists = WatchlistCore(config.get("watchlists", {}))

    def init_all(self) -> None:
        LOGGER.info("Inicializando servicios núcleo de M82...")
        self.ledger.start()
        self.sentinels.start()
        self.watchlists.start()
        LOGGER.info("Servicios núcleo inicializados.")

    def snapshot_state(self) -> Dict[str, Any]:
        snapshot = {
            "ts": datetime.now(timezone.utc).isoformat(),  # Actualizado
            "env": self.env,
            "state": self.state,
        }
        try:
            os.makedirs(os.path.dirname(RUNTIME_STATE_FILE), exist_ok=True)
            with open(RUNTIME_STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, indent=2, ensure_ascii=False)
        except Exception as e:
            LOGGER.exception("Error guardando runtime_state: %s", e)
        return snapshot

# -------------------------------------------------------------------------
#  Ciclo principal
# -------------------------------------------------------------------------

def main_loop(ctx: M82Context) -> None:
    loop_sleep = float(ctx.config.get("loop_sleep_seconds", 1.0))
    ledger_interval = int(ctx.config.get("ledger_snapshot_interval", 60))
    iteration = 0

    LOGGER.info(
        "Entrando al loop principal. loop_sleep=%.2fs, ledger_interval=%d",
        loop_sleep,
        ledger_interval,
    )

    while not SHUTDOWN.is_triggered():
        iteration += 1
        loop_ts = datetime.now(timezone.utc)  # Actualizado

        try:
            ctx.sentinels.tick()
            ctx.watchlists.refresh()

            while True:
                evt = EVENT_BUS.get(timeout=0.001)
                if not evt:
                    break
                LOGGER.debug("Evento interno recibido: %s", evt)

            if iteration % ledger_interval == 0:
                snapshot = ctx.snapshot_state()
                ctx.ledger.record_snapshot(snapshot)
                iteration = 0 

            ctx.state["last_loop_ts"] = loop_ts.isoformat()
            ctx.state["loop_iteration"] = iteration

        except Exception as e:
            LOGGER.exception("Error en iteración del loop principal: %s", e)
            ctx.state["last_error"] = {
                "ts": datetime.now(timezone.utc).isoformat(),  # Actualizado
                "msg": str(e),
            }

        time.sleep(loop_sleep)

    LOGGER.info("Loop principal finalizado. Iteraciones totales (ciclo final): %d", iteration)

# -------------------------------------------------------------------------
#  Entry point
# -------------------------------------------------------------------------

def main() -> int:
    LOGGER.info("=== M82 Sovereign Core – Monolith: START ===")
    LOGGER.info("Working dir: %s", BASE_DIR)

    try:
        ctx = M82Context(GLOBAL_CONFIG)
        ctx.init_all()
        main_loop(ctx)
    except Exception as e:
        LOGGER.exception("Fallo crítico en M82 monolith: %s", e)
        return 1
    finally:
        LOGGER.info("=== M82 Sovereign Core – Monolith: STOP ===")

    return 0


if __name__ == "__main__":
    sys.exit(main())
