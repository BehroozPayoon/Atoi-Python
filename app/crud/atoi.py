class Atoi:
    def set_item(self,redis_con, input_str: str, result: str):
        redis_con.set(input_str, result)

    def get_item(self,redis_con, input_str: str):
        return redis_con.get(input_str)

atoi = Atoi()