

class PR:
    def __init__(self, pr_id: int, user_id: int, half_pr, full_pr, fiftyk_pr, fiftym_pr, hundredk_pr, hundredm_pr, about_me):
        self.pr_id = pr_id
        self.user_id = user_id
        self.half_pr =  half_pr
        self.full_pr =  full_pr
        self.fiftyk_pr = fiftyk_pr
        self.fiftym_pr = fiftym_pr
        self.hundredk_pr = hundredk_pr
        self.hundredm_pr = hundredm_pr
        self.about_me = about_me
    
    def __repr__(self) -> str:
        return f"User PR Info: {self.pr_id} + {self.user_id} + {self.half_pr}+ {self.full_pr} + {self.fiftyk_pr} + {self.fiftym_pr} + {self.hundredk_pr} + {self.hundredm_pr}"

