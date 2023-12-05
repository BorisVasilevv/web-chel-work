class CategoryWithSubcategories:
    id: int
    category_name: str
    style_name: str
    description: str
    subcategories = []

    def __init__(self, categor_id, categor_name, categor_style_name, categor_description):
        self.id = categor_id
        self.category_name = categor_name
        self.style_name = categor_style_name
        self.description = categor_description
