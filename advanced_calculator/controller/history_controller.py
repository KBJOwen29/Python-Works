import database.database as Database


class HistoryController:
    def get_all(self):
        return Database.get_all_calculations()

    def get_by_id(self, calculation_id):
        return Database.get_calculation(calculation_id)

    def search(self, term):
        return Database.search_calculations(term)

    def delete(self, calculation_id):
        return Database.delete_calculation(calculation_id)

    def clear(self):
        return Database.clear_history()
