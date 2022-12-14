from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base, metadata


class Conteudo(Base):

    __tablename__ = 'conteudo'
    metadata = metadata

    cd_conteudo = Column(Integer, index=True, primary_key=True)
    cd_tipo_conteudo = Column(Integer, ForeignKey("tipo_conteudo.cd_tipo_conteudo"))
    tipo_conteudo = relationship("TipoConteudo", back_populates='conteudos')
    dc_titulo_conteudo = Column(String)
    tx_conteudo = Column(String)
    aq_imagem_conteudo = Column(String) 
    aq_conteudo = Column(String) 
    dt_atualizacao = Column(String)
    #nm_ordem_conteudo = Column(String) --> está vazio em todos

    cd_tipo_situacao = Column(Integer)

class TipoConteudo(Base):

    __tablename__ = 'tipo_conteudo'
    metadata = metadata

    cd_tipo_conteudo = Column(Integer, index=True, primary_key=True)
    sg_tipo_conteudo = Column(String)
    dc_tipo_conteudo = Column(String)
    conteudos = relationship("Conteudo", back_populates='tipo_conteudo')

class ParametrosSistema(Base):

    __tablename__ = 'parametro_sistema'
    metadata = metadata

    cd_parametro_sistema = Column(Integer, index=True, primary_key=True)
    cd_chave_parametro = Column(String)
    dc_chave_parametro = Column(String)
    vl_chave_parametro = Column(String)