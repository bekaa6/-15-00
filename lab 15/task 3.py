from abc import ABC, abstractmethod



class DigitalProduct(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass



class VideoContent(DigitalProduct):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_info(self) -> str:
        return f"Видео: '{self.title}' (Ұзақтығы: {self.duration} минут)"



class AudioContent(DigitalProduct):
    def __init__(self, title, bitrate):
        self.title = title
        self.bitrate = bitrate

    def get_info(self) -> str:
        return f"Аудио: '{self.title}' (Битрейт: {self.bitrate} kbps)"



class ProductFactory:


    def create_product(self, product_type: str, **kwargs) -> DigitalProduct:
        product_type = product_type.lower()

        if product_type == "video":
            return VideoContent(kwargs.get("title"), kwargs.get("duration"))
        elif product_type == "audio":
            return AudioContent(kwargs.get("title"), kwargs.get("bitrate"))
        else:
            raise ValueError(f"Белгісіз өнім түрі: {product_type}")



if __name__ == "__main__":
    factory = ProductFactory()

    video = factory.create_product(
        "video",
        title="Python Design Patterns",
        duration=45
    )

    audio = factory.create_product(
        "audio",
        title="Software Architecture Podcast",
        bitrate=192
    )

    print(video.get_info())
    print(audio.get_info())