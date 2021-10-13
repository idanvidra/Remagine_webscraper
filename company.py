class company:
    def __init__(self) -> None:
        name = ""
        page_url = ""
        link = ""
        about = ""
        team_list = []
        year_founded = ""
        business_model_list = []
        employees = ""
        funding_stage = ""
        product_stage = ""
        funds_raised = ""

    def to_string(this):
        # Printing
        print("Name:")
        print(this.name)

        print("URL:")
        print(this.page_url)

        print("Business model:")
        print(this.business_model)

        print("Year founded:")
        print(this.year_founded)

        print("About:")
        print(this.about)

        print("# of employees:")
        print(this.employees)

        print("Funding stage:")
        print(this.funding_stage)

        print("Funding raised:")
        print(this.funds_raised)

        print("Product stage:")
        print(this.product_stage)

        print("Team:")
        print(this.link)
