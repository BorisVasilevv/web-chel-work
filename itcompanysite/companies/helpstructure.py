
class CompanyWithFavoriteFlag:
    id: int
    name: str
    logotype: str
    short_description: str
    url: str
    is_favorite: bool

    def __init__(self, company_id, company_name, company_logotype, company_short_description, company_url, company_is_favorite):
        self.id = company_id
        self.name = company_name
        self.logotype = company_logotype
        self.short_description = company_short_description
        self.url = company_url
        self.is_favorite = company_is_favorite
