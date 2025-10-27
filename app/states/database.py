import reflex as rx
import os
import logging
from sqlalchemy import create_engine, text
from typing import Any, Optional


class DatabaseState(rx.State):
    """State for database operations"""

    db_connected: bool = False
    connection_status: str = "Not connected"

    @rx.event
    async def check_database_connection(self):
        """Check if database is connected and accessible"""
        try:
            db_url = os.getenv("REFLEX_DB_URL")
            if not db_url:
                self.connection_status = "REFLEX_DB_URL environment variable not set"
                self.db_connected = False
                return
            engine = create_engine(db_url)
            with engine.connect() as conn:
                result = conn.execute(text("SELECT 1"))
                if result.fetchone():
                    self.connection_status = "Connected successfully"
                    self.db_connected = True
                else:
                    self.connection_status = "Connection test failed"
                    self.db_connected = False
        except Exception as e:
            logging.exception(f"Database connection error: {e}")
            self.connection_status = f"Connection error: {str(e)}"
            self.db_connected = False

    @rx.event
    async def execute_query(self, query: str) -> list[dict[str, Any]]:
        """Execute a SELECT query and return results"""
        try:
            db_url = os.getenv("REFLEX_DB_URL")
            if not db_url:
                logging.error("REFLEX_DB_URL not set")
                return []
            engine = create_engine(db_url)
            with engine.connect() as conn:
                result = conn.execute(text(query))
                columns = result.keys()
                rows = result.fetchall()
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logging.exception(f"Query execution error: {e}")
            return []