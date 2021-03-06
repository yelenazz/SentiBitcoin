import traceback

from db_manager import Connection
from utils import PCKL_ADNOTAD_FILENAME_START
from trainers.trainer_general import train_classifier


if __name__ == "__main__":
    conn = Connection()
    collection = conn.get_english_collection()

    try:
        train_classifier(collection=collection, filename_start=PCKL_ADNOTAD_FILENAME_START,
            main_cat_name="ADVERT", main_cat_filenames=["..\\training_data\\ad.txt"],
            opposite_cat_name="NOT_AD", opposite_cat_filenames=[
                "..\\training_data\\positive.txt", "..\\training_data\\negative.txt",
                "..\\training_data\\neutral.txt", "..\\training_data\\news.txt"
            ])
    except:
        traceback.print_exc()
    finally:
        conn.close_connection()
