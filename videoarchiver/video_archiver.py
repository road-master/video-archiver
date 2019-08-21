from videoarchiver import CONFIG, Directory
from videoarchiver.niconico.archive_step import ArchiveStep
from videoarchiver.tvasahi.client_for_back_end import ClientForBackEnd


class VideoArchiver:
    @staticmethod
    def execute():
        CONFIG.load()
        archive_step = ArchiveStep(ClientForBackEnd, Directory.DOWNLOAD.value)
        archive_step.execute()
