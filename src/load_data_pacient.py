from schema import PacientDataCreateSchema, PacientDataReadSchema, PacientDataUpdateSchema
import json


class SaveDataPacient:
    def get_pacients(self, pacient: PacientDataCreateSchema) -> list[PacientDataReadSchema]:
        with open("db_pacients.json") as file:
            db = json.load(file)
        return db 

    def create_data_pacient(self, pacient: PacientDataCreateSchema) -> dict:
        with open("db_pacients.json") as file:
            db = json.load(file)
            pacient_dict = pacient.model_dump()
        # pacient_dict = {
        #     name: str,
        #     age: int, 
        #     med_history: str,
        #     story_life: str, 
        #     symptoms: str, 
        #     local_status: str, 
        #     diagnosis: str, 
        #     med_tactis: str, 
        #     med_final: str 
        # }
        db.append(pacient_dict)
        with open("db_pacients.json", "w") as file:
            json.dump(db, file, indent=4, ensure_ascii=False)
        return pacient_dict

    

        