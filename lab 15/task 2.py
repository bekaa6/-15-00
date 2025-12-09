from abc import ABC, abstractmethod
import json
import csv
from io import StringIO


class ExportStrategy(ABC):
    @abstractmethod
    def export(self, data: list[dict]) -> str:
        pass



class JsonExportStrategy(ExportStrategy):
    def export(self, data: list[dict]) -> str:
        print("--- JSON Export Strategy іске қосылды ---")
        return json.dumps(data, indent=4, ensure_ascii=False)



class CsvExportStrategy(ExportStrategy):
    def export(self, data: list[dict]) -> str:
        print("--- CSV Export Strategy іске қосылды ---")
        if not data: return ""

        output = StringIO()
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()



class ReportExporter:
    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        """Стратегияны ауыстыру"""
        self._strategy = strategy

    def export_report(self, data: list[dict]):
        """Таңдалған стратегияны орындау"""
        return self._strategy.export(data)



if __name__ == "__main__":
    sample_data = [
        {"id": 1, "product": "Ноутбук", "price": 1200},
        {"id": 2, "product": "Телефон", "price": 800},
    ]

    exporter = ReportExporter(JsonExportStrategy())
    json_output = exporter.export_report(sample_data)
    print("\n[JSON Экспорт]:\n", json_output)

    exporter.set_strategy(CsvExportStrategy())
    csv_output = exporter.export_report(sample_data)
    print("\n[CSV Экспорт]:\n", csv_output)