import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from current directory and module directory
load_dotenv()
load_dotenv(Path(__file__).resolve().parent / ".env")

# Centralized configuration for the agent
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.7-flash")

# Database configuration
DB_DIALECT = os.getenv("DB_DIALECT", "sqlite").lower()
DB_URI = os.getenv("DB_URI", "src/texttosql/sakila_master.db")
