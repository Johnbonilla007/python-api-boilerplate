import sys
import os
import importlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.infrastructure.database import Base  # Importar Base correctamente

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config

def import_all_models(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.models.{filename[:-3]}"
            importlib.import_module(module_name)

# Importar todos los modelos en el directorio app.models
import_all_models(os.path.join(os.path.dirname(__file__), "../app/models"))

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata  # Ahora sí se encuentra Base

def run_migrations_offline() -> None:
    """Ejecutar migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Ejecutar migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()



