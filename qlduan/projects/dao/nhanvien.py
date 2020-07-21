class Nhanvien:
    _id = None
    _name = None
    _birthdate = None
    _birthplace = None
    _hometown = None
    _address = None
    _email = None
    _phone = None
    _team = None
    _ten_chucvu = None
    _avatar = None
    _duans = []

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
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value):
        self._birthdate = value
    
    @property
    def birthplace(self):
        return self._birthplace

    @birthplace.setter
    def birthplace(self, value):
        self._birthplace = value
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        self._hometown = value
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def ten_chucvu(self):
        return self._ten_chucvu
    
    @ten_chucvu.setter
    def ten_chucvu(self, value):
        self._ten_chucvu = value
    @property

    def avatar(self):
        return self._avatar
    
    @avatar.setter
    def avatar(self, value):
        self._avatar = value

    @property
    def duans(self):
        return self._duans
    
    @duans.setter
    def duans(self, value):
        self._duans = value