from sqlalchemy.engine.base import Engine

from package.services.db.db import ConnBigDataCieg, ConnCiegDev, ConnTrilhasAuditoria


def test_conn_big_data_cieg():
    """Testa a conexão com o banco de dados BIG_DATA_CIEG."""
    conn = ConnBigDataCieg()
    engine = conn.get_engine()
    assert isinstance(engine, Engine)


def test_conn_cieg_dev():
    """Testa a conexão com o banco de dados CIEG_DEV."""
    conn = ConnCiegDev()
    engine = conn.get_engine()
    assert isinstance(engine, Engine)


def test_conn_trilhas_auditoria():
    """Testa a conexão com o banco de dados TRILHAS_AUDITORIA."""
    conn = ConnTrilhasAuditoria()
    engine = conn.get_engine()
    assert isinstance(engine, Engine)
