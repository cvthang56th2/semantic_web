class DuAn:
    _id = None
    _name = None
    _ngon_ngu = None
    _summary = None
    _team = None
    _year = None
    _nhanviens = []

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def ngon_ngu(self):
        return self._ngon_ngu

    @ngon_ngu.setter
    def ngon_ngu(self, value):
        self._ngon_ngu = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def nhanviens(self):
        return self._nhanviens

    @nhanviens.setter
    def nhanviens(self, value):
        self._nhanviens = value
