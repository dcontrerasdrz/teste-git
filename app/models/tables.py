from app import db


class Usuario(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(50), unique=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))
    condicao = db.Column(db.String(50))

    @property
    def is_authenticate(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self,usuario,nome,email,senha,condicao):
        self.usuario=usuario
        self.nome=nome
        self.email=email
        self.senha=senha
        self.condicao=condicao

    def __repr__(self):
        return '<Usuario %r>' % self.usuario


        
class Pereciveis(db.Model):

    __tablename__ = "pereciveis"
    id=db.Column(db.Integer,primary_key=True)
    Departamento=db.Column(db.String(210))
    Setor=db.Column(db.String(230))
    Grupo=db.Column(db.String(260))
    Familia=db.Column(db.String(280))
    Subfamilia=db.Column(db.String(300))
    Tp_Pessoa=db.Column(db.String(200))
    Cpf_Cnpj=db.Column(db.String(340))
    Cod_Forn=db.Column(db.String(200))
    Tipo_De_Contrato_Ancf=db.Column(db.String(200))
    Contrato=db.Column(db.String(200))
    Filial_Fornec=db.Column(db.String(200))
    Natureza=db.Column(db.String(200))
    Codigo_Do_Sad=db.Column(db.String(260))
    Tipo_De_Produto_Sad=db.Column(db.String(210))
    Tipo_De_Produto=db.Column(db.String(210))
    Tipo_Ean_Sad=db.Column(db.String(210))
    Tipo_De_Ean=db.Column(db.String(210))
    Gtin=db.Column(db.String(250))
    Gtin_Upc=db.Column(db.String(250))
    Descricao_Reduzida=db.Column(db.String(320))
    Referencia=db.Column(db.String(360))
    Codigo_Do_Modelo=db.Column(db.String(200))
    Procedencia=db.Column(db.String(210))
    Pais_De_Origem=db.Column(db.String(200))
    Cert_Origem=db.Column(db.String(200))
    Cert_Conformidade=db.Column(db.String(200))
    Ppb=db.Column(db.String(200))
    Voltagem=db.Column(db.String(200))
    Tp_Embal_Compra=db.Column(db.String(240))
    Qtd_Por_Embalag_Compra=db.Column(db.String(220))
    Dimensao_Altura_Valor_Metro=db.Column(db.String(240))
    Dimensao_Largura_Valor_Metro=db.Column(db.String(240))
    Dimensao_Comprimento_Valor_Metro=db.Column(db.String(240))
    Peso_Valor_Quilo=db.Column(db.String(230))
    Qtd_Base=db.Column(db.String(220))
    Qtd_Altura=db.Column(db.String(220))
    Qtd_Total=db.Column(db.String(230))
    Marca=db.Column(db.String(430))
    Qtd_Por_Embalag_Venda=db.Column(db.String(220))
    Dimensao_Altura_Unidade=db.Column(db.String(230))
    Dimensao_Largura_Unidade=db.Column(db.String(230))
    Dimensao_Comprimento_Unidade=db.Column(db.String(230))
    Volume=db.Column(db.String(200))
    Dimensao_Altura_Valor=db.Column(db.String(230))
    Dimensao_Largura_Valor=db.Column(db.String(230))
    Dimensao_Comprimento_Valor=db.Column(db.String(230))
    Peso_Valor=db.Column(db.String(210))
    Dun14=db.Column(db.String(350))
    Temperatura_Minima=db.Column(db.String(200))
    Temperatura_Maxima=db.Column(db.String(200))
    Empilhamento_Maximo=db.Column(db.String(200))
    Vida_Util=db.Column(db.String(230))
    Prazo_De_Consumo=db.Column(db.String(230))
    Cod_Rms=db.Column(db.String(200))
    Cod_Root=db.Column(db.String(200))
    Id_Big=db.Column(db.String(200))
    Palavra_big=db.Column(db.String(350))
    Depto_carrefour=db.Column(db.String(210))
    Cod_Setcarrefour=db.Column(db.String(240))
    Desc_Setor_carrefour=db.Column(db.String(310))
    Cod_Grupo_carrefour=db.Column(db.String(260))
    Desc_Grupo_carrefour=db.Column(db.String(460))
    Cod_Familia_carrefour=db.Column(db.String(28))
    Desc_Familia_carrefour=db.Column(db.String(540))
    Cod_Sub_Familia_carrefour=db.Column(db.String(300))
    Sub_Familia_carrefour=db.Column(db.String(700))
    Cod_Eancarrefour=db.Column(db.String(330))
    Br_Ean_1_carrefour=db.Column(db.String(200))
    Br_Ean_2_carrefour=db.Column(db.String(200))
    Br_Ean_3_carrefour=db.Column(db.String(200))
    Br_Ean_4_carrefour=db.Column(db.String(200))
    Unidade_De_Estoque=db.Column(db.String(260))
    Br_Ean_5_carrefour=db.Column(db.String(200))
    Cnpj_Fornec_carrefour=db.Column(db.String(340))
    Nom_Razao_Social_Fornecedor_carrefour=db.Column(db.String(300))
    Cod_Rms_Fornec_carrefour=db.Column(db.String(270))
    Tipo_ean_carrefour=db.Column(db.String(210))
    Desc_Tipo_Ean_carrefour=db.Column(db.String(230))
    Tp_Prod_carrefour=db.Column(db.String(220))
    Desc_Tpo_carrefour=db.Column(db.String(330))
    Cod_Rms_Produto_carrefour=db.Column(db.String(270))
    Cod_Int_Gold_carrefour=db.Column(db.String(280))
    Ecom_carrefour=db.Column(db.String(330))
    Cod_Status_carrefour=db.Column(db.String(210))
    Dsc_Status_carrefour=db.Column(db.String(270))
    Tp_Emb_carrefour=db.Column(db.String(220))
    Cod_Uni_Med_Emb_carrefour=db.Column(db.String(230))
    Dsc_Uni_Med_Emb_carrefour=db.Column(db.String(300))
    Compr_carrefour=db.Column(db.String(250))
    Larg_carrefour=db.Column(db.String(240))
    Altur_carrefour=db.Column(db.String(240))
    Peso_carrefour=db.Column(db.String(240))
    Dsc_Uni_Peso_carrefour=db.Column(db.String(270))
    Sazonal_carrefour=db.Column(db.String(320))
    Abrangencia_carrefour=db.Column(db.String(300))
    Prod_514_Carrefour=db.Column(db.String(200))
    Super_Nosso_carrefour=db.Column(db.String(330))
    Palavra_crf_carrefour=db.Column(db.String(320))
    Cod_Ncm_carrefour=db.Column(db.String(320))
    Descricao_Rms_carrefour=db.Column(db.String(100))
    Descricao_Rms_Higienizada_carrefour=db.Column(db.String(550))
    Ncm=db.Column(db.String(280))
    Descricao_Completa=db.Column(db.String(550))
    Descricao_Completa_Higienizada=db.Column(db.String(610))
    Match_Score=db.Column(db.String(230))
    Tp_Embal_Venda=db.Column(db.String(240))
    BIG_EST_MERC=db.Column(db.String(300))
    BIG_DEPARTAMENTO=db.Column(db.String(480))
    BIG_NOME_PORTFOLIO=db.Column(db.String(410))
    BIG_NOME_SECAO=db.Column(db.String(430))
    BIG_NOME_LINHA=db.Column(db.String(500))
    BIG_NOME_SUBLINHA=db.Column(db.String(490))
    DSRelacVinc_1=db.Column(db.String(330))
    DSRelacVinc_2=db.Column(db.String(360))
    DSRelacVinc_3=db.Column(db.String(340))
    ItemRelacionado=db.Column(db.String(2710))
    DSRelacTransfder_1=db.Column(db.String(330))
    DSRelacTransfder_2=db.Column(db.String(360))
    DSRelacTransfder_3=db.Column(db.String(340))
    ItemRelacionadoTransfDerivado=db.Column(db.String(4450))
    Aprovacao=db.Column(db.String(500))
    Observacao=db.Column(db.String(347))
	


    def __init__(self,Departamento,Setor,Grupo,Familia,Subfamilia,Tp_Pessoa,Cpf_Cnpj,Cod_Forn,Tipo_De_Contrato_Ancf,Contrato,Filial_Fornec,Natureza,Codigo_Do_Sad,Tipo_De_Produto_Sad,Tipo_De_Produto,Tipo_Ean_Sad,Tipo_De_Ean,Gtin,Gtin_Upc,Descricao_Reduzida,Referencia,Codigo_Do_Modelo,Procedencia,Pais_De_Origem,Cert_Origem,Cert_Conformidade,Ppb,Voltagem,Tp_Embal_Compra,Qtd_Por_Embalag_Compra,Dimensao_Altura_Valor_Metro,Dimensao_Largura_Valor_Metro,Dimensao_Comprimento_Valor_Metro,Peso_Valor_Quilo,Qtd_Base,Qtd_Altura,Qtd_Total,Marca,Qtd_Por_Embalag_Venda,Dimensao_Altura_Unidade,Dimensao_Largura_Unidade,Dimensao_Comprimento_Unidade,Volume,Dimensao_Altura_Valor,Dimensao_Largura_Valor,Dimensao_Comprimento_Valor,Peso_Valor,Dun14,Temperatura_Minima,Temperatura_Maxima,Empilhamento_Maximo,Vida_Util,Prazo_De_Consumo,Cod_Rms,Cod_Root,Id_Big,Palavra_big,Depto_carrefour,Cod_Setcarrefour,Desc_Setor_carrefour,Cod_Grupo_carrefour,Desc_Grupo_carrefour,Cod_Familia_carrefour,Desc_Familia_carrefour,Cod_Sub_Familia_carrefour,Sub_Familia_carrefour,Cod_Eancarrefour,Br_Ean_1_carrefour,Br_Ean_2_carrefour,Br_Ean_3_carrefour,Br_Ean_4_carrefour,Unidade_De_Estoque,Br_Ean_5_carrefour,Cnpj_Fornec_carrefour,Nom_Razao_Social_Fornecedor_carrefour,Cod_Rms_Fornec_carrefour,Tipo_ean_carrefour,Desc_Tipo_Ean_carrefour,Tp_Prod_carrefour,Desc_Tpo_carrefour,Cod_Rms_Produto_carrefour,Cod_Int_Gold_carrefour,Ecom_carrefour,Cod_Status_carrefour,Dsc_Status_carrefour,Tp_Emb_carrefour,Cod_Uni_Med_Emb_carrefour,Dsc_Uni_Med_Emb_carrefour,Compr_carrefour,Larg_carrefour,Altur_carrefour,Peso_carrefour,Dsc_Uni_Peso_carrefour,Sazonal_carrefour,Abrangencia_carrefour,Prod_514_Carrefour,Super_Nosso_carrefour,Palavra_crf_carrefour,Cod_Ncm_carrefour,Descricao_Rms_carrefour,Descricao_Rms_Higienizada_carrefour,Ncm,Descricao_Completa,Descricao_Completa_Higienizada,Match_Score,Tp_Embal_Venda,BIG_EST_MERC,BIG_DEPARTAMENTO,BIG_NOME_PORTFOLIO,BIG_NOME_SECAO,BIG_NOME_LINHA,BIG_NOME_SUBLINHA,DSRelacVinc_1,DSRelacVinc_2,DSRelacVinc_3,ItemRelacionado,DSRelacTransfder_1,DSRelacTransfder_2,DSRelacTransfder_3,ItemRelacionadoTransfDerivado,Aprovacao,Observacao):

        self.Departamento=Departamento
        self.Setor=Setor
        self.Grupo=Grupo
        self.Familia=Familia
        self.Subfamilia=Subfamilia
        self.Tp_Pessoa=Tp_Pessoa
        self.Cpf_Cnpj=Cpf_Cnpj
        self.Cod_Forn=Cod_Forn
        self.Tipo_De_Contrato_Ancf=Tipo_De_Contrato_Ancf
        self.Contrato=Contrato
        self.Filial_Fornec=Filial_Fornec
        self.Natureza=Natureza
        self.Codigo_Do_Sad=Codigo_Do_Sad
        self.Tipo_De_Produto_Sad=Tipo_De_Produto_Sad
        self.Tipo_De_Produto=Tipo_De_Produto
        self.Tipo_Ean_Sad=Tipo_Ean_Sad
        self.Tipo_De_Ean=Tipo_De_Ean
        self.Gtin=Gtin
        self.Gtin_Upc=Gtin_Upc
        self.Descricao_Reduzida=Descricao_Reduzida
        self.Referencia=Referencia
        self.Codigo_Do_Modelo=Codigo_Do_Modelo
        self.Procedencia=Procedencia
        self.Pais_De_Origem=Pais_De_Origem
        self.Cert_Origem=Cert_Origem
        self.Cert_Conformidade=Cert_Conformidade
        self.Ppb=Ppb
        self.Voltagem=Voltagem
        self.Tp_Embal_Compra=Tp_Embal_Compra
        self.Qtd_Por_Embalag_Compra=Qtd_Por_Embalag_Compra
        self.Dimensao_Altura_Valor_Metro=Dimensao_Altura_Valor_Metro
        self.Dimensao_Largura_Valor_Metro=Dimensao_Largura_Valor_Metro
        self.Dimensao_Comprimento_Valor_Metro=Dimensao_Comprimento_Valor_Metro
        self.Peso_Valor_Quilo=Peso_Valor_Quilo
        self.Qtd_Base=Qtd_Base
        self.Qtd_Altura=Qtd_Altura
        self.Qtd_Total=Qtd_Total
        self.Marca=Marca
        self.Qtd_Por_Embalag_Venda=Qtd_Por_Embalag_Venda
        self.Dimensao_Altura_Unidade=Dimensao_Altura_Unidade
        self.Dimensao_Largura_Unidade=Dimensao_Largura_Unidade
        self.Dimensao_Comprimento_Unidade=Dimensao_Comprimento_Unidade
        self.Volume=Volume
        self.Dimensao_Altura_Valor=Dimensao_Altura_Valor
        self.Dimensao_Largura_Valor=Dimensao_Largura_Valor
        self.Dimensao_Comprimento_Valor=Dimensao_Comprimento_Valor
        self.Peso_Valor=Peso_Valor
        self.Dun14=Dun14
        self.Temperatura_Minima=Temperatura_Minima
        self.Temperatura_Maxima=Temperatura_Maxima
        self.Empilhamento_Maximo=Empilhamento_Maximo
        self.Vida_Util=Vida_Util
        self.Prazo_De_Consumo=Prazo_De_Consumo
        self.Cod_Rms=Cod_Rms
        self.Cod_Root=Cod_Root
        self.Id_Big=Id_Big
        self.Palavra_big=Palavra_big
        self.Depto_carrefour=Depto_carrefour
        self.Cod_Setcarrefour=Cod_Setcarrefour
        self.Desc_Setor_carrefour=Desc_Setor_carrefour
        self.Cod_Grupo_carrefour=Cod_Grupo_carrefour
        self.Desc_Grupo_carrefour=Desc_Grupo_carrefour
        self.Cod_Familia_carrefour=Cod_Familia_carrefour
        self.Desc_Familia_carrefour=Desc_Familia_carrefour
        self.Cod_Sub_Familia_carrefour=Cod_Sub_Familia_carrefour
        self.Sub_Familia_carrefour=Sub_Familia_carrefour
        self.Cod_Eancarrefour=Cod_Eancarrefour
        self.Br_Ean_1_carrefour=Br_Ean_1_carrefour
        self.Br_Ean_2_carrefour=Br_Ean_2_carrefour
        self.Br_Ean_3_carrefour=Br_Ean_3_carrefour
        self.Br_Ean_4_carrefour=Br_Ean_4_carrefour
        self.Unidade_De_Estoque=Unidade_De_Estoque
        self.Br_Ean_5_carrefour=Br_Ean_5_carrefour
        self.Cnpj_Fornec_carrefour=Cnpj_Fornec_carrefour
        self.Nom_Razao_Social_Fornecedor_carrefour=Nom_Razao_Social_Fornecedor_carrefour
        self.Cod_Rms_Fornec_carrefour=Cod_Rms_Fornec_carrefour
        self.Tipo_ean_carrefour=Tipo_ean_carrefour
        self.Desc_Tipo_Ean_carrefour=Desc_Tipo_Ean_carrefour
        self.Tp_Prod_carrefour=Tp_Prod_carrefour
        self.Desc_Tpo_carrefour=Desc_Tpo_carrefour
        self.Cod_Rms_Produto_carrefour=Cod_Rms_Produto_carrefour
        self.Cod_Int_Gold_carrefour=Cod_Int_Gold_carrefour
        self.Ecom_carrefour=Ecom_carrefour
        self.Cod_Status_carrefour=Cod_Status_carrefour
        self.Dsc_Status_carrefour=Dsc_Status_carrefour
        self.Tp_Emb_carrefour=Tp_Emb_carrefour
        self.Cod_Uni_Med_Emb_carrefour=Cod_Uni_Med_Emb_carrefour
        self.Dsc_Uni_Med_Emb_carrefour=Dsc_Uni_Med_Emb_carrefour
        self.Compr_carrefour=Compr_carrefour
        self.Larg_carrefour=Larg_carrefour
        self.Altur_carrefour=Altur_carrefour
        self.Peso_carrefour=Peso_carrefour
        self.Dsc_Uni_Peso_carrefour=Dsc_Uni_Peso_carrefour
        self.Sazonal_carrefour=Sazonal_carrefour
        self.Abrangencia_carrefour=Abrangencia_carrefour
        self.Prod_514_Carrefour=Prod_514_Carrefour
        self.Super_Nosso_carrefour=Super_Nosso_carrefour
        self.Palavra_crf_carrefour=Palavra_crf_carrefour
        self.Cod_Ncm_carrefour=Cod_Ncm_carrefour
        self.Descricao_Rms_carrefour=Descricao_Rms_carrefour
        self.Descricao_Rms_Higienizada_carrefour=Descricao_Rms_Higienizada_carrefour
        self.Ncm=Ncm
        self.Descricao_Completa=Descricao_Completa
        self.Descricao_Completa_Higienizada=Descricao_Completa_Higienizada
        self.Match_Score=Match_Score
        self.Tp_Embal_Venda=Tp_Embal_Venda
        self.BIG_EST_MERC=BIG_EST_MERC
        self.BIG_DEPARTAMENTO=BIG_DEPARTAMENTO
        self.BIG_NOME_PORTFOLIO=BIG_NOME_PORTFOLIO
        self.BIG_NOME_SECAO=BIG_NOME_SECAO
        self.BIG_NOME_LINHA=BIG_NOME_LINHA
        self.BIG_NOME_SUBLINHA=BIG_NOME_SUBLINHA
        self.DSRelacVinc_1=DSRelacVinc_1
        self.DSRelacVinc_2=DSRelacVinc_2
        self.DSRelacVinc_3=DSRelacVinc_3
        self.ItemRelacionado=ItemRelacionado
        self.DSRelacTransfder_1=DSRelacTransfder_1
        self.DSRelacTransfder_2=DSRelacTransfder_2
        self.DSRelacTransfder_3=DSRelacTransfder_3
        self.ItemRelacionadoTransfDerivado=ItemRelacionadoTransfDerivado
        self.Aprovacao=Aprovacao
        self.Observacao=Observacao