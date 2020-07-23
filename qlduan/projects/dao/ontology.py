from owlready2 import *
# from rdflib import *
from .nhanvien import Nhanvien
from .duan import DuAn
from .team import Team

def get_value(value):
    if len(value) > 0:
        return value[0]

def build_team(data, fetch=False):
    team = Team()
    team.id = data._name
    team.name = get_value(data.TEN_TEAM)

    if fetch:
        nhanviens = []
        for item in data.team_co_nv:
            nv = build_nhanvien(item)
            nhanviens.append(nv)
        team.nhanviens = nhanviens

        duans = []
        for item in data.team_tao_ra_duan:
            da = build_duan(item)
            duans.append(da)
        team.duans = duans
    return team

def build_nhanvien(data, fetch=False):
    nv = Nhanvien()
    nv.id = data._name
    nv.name = get_value(data.HO_TEN)
    if get_value(data.NGAY_SINH):
        nv.birthdate = get_value(data.NGAY_SINH).strftime('%d/%m/%Y')
    nv.birthplace = get_value(data.NOI_SINH)
    nv.hometown = get_value(data.QUE_QUAN)
    nv.address = get_value(data.DIA_CHI)
    nv.email = get_value(data.EMAIL)
    nv.phone = get_value(data.SDT)
    nv.avatar = get_value(data.avatar)

    if fetch:
        if data.nv_thuoc_team:
            nv.team = build_team(data.nv_thuoc_team[0], True)
            cv = get_value(data.NV_co_CV)
            if cv:
                nv.ten_chucvu = get_value(cv.TEN_CV)

            nv.duans = nv.team.duans
    return nv

def build_duan(data, fetch=False):
    da = DuAn()
    da.id = data._name
    da.name = get_value(data.TEN_DA)
    da.ngon_ngu = get_value(data.ngon_ngu)
    da.summary = get_value(data.tom_tat)
    
    if fetch:
        da.team = build_team(data.duan_tao_ra_boi_team[0], True)
        if da.team:
            da.ten_team_tao_ra = da.team.name
            da.nhanviens = da.team.nhanviens
    return da

class Ontology:
    def __init__(self, filename):
        self.world = World()
        self.onto = self.world.get_ontology(filename).load()
        self.graph = self.world.as_rdflib_graph()
    
    def search_nhanviens(self, query):
        computedQuery = str(query).title()
        queryString = 'PREFIX dt:<http://www.semanticweb.org/quanlidetai#> SELECT ?tennv WHERE { ?tennv dt:HO_TEN ?ten FILTER regex(?ten, "%s")}' % computedQuery
        result = list(self.graph.query(queryString))

        nhanviens = []
        for item in result:
            nv = build_nhanvien(self.world[str(item['tennv'])], True)
            nhanviens.append(nv)
        return nhanviens

    def get_nhanviens(self):
        nhanviens = []
        for item in self.onto.NHAN_VIEN.instances():
            nv = build_nhanvien(item, True)
            nhanviens.append(nv)
        return nhanviens

    def get_nhanvien(self, id):
        item = self.onto.NHAN_VIEN(id)
        return build_nhanvien(item, fetch=True)

    def search_duans(self, query):
        computedQuery = str(query).title()
        queryString = 'PREFIX dt:<http://www.semanticweb.org/quanlidetai#> SELECT ?tenda WHERE { ?tenda dt:TEN_DA ?ten FILTER regex(?ten, "%s")}' % computedQuery
        result = list(self.graph.query(queryString))

        duans = []
        for item in result:
            da = build_duan(self.world[str(item['tenda'])], fetch=True)
            duans.append(da)
        return duans

    def get_duans(self):
        duans = []
        for item in self.onto.DUAN.instances():
            da = build_duan(item, fetch=True)
            duans.append(da)
        return duans

    def get_duan(self, id):
        item = self.onto.DUAN(id)
        return build_duan(item, fetch=True)

    def get_teams(self):
        teams = []
        for item in self.onto.TEAM.instances():
            team = build_team(item)
            teams.append(team)
        return teams
    
    def get_team(self, id):
        item = self.onto.TEAM(id)
        return build_team(item, fetch=True)
