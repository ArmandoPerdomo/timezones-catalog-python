import pytz
import csv
from geopy.geocoders import Nominatim
import logging
import json
from googletrans import Translator
from continent_mappings import get_country_and_continent_from_timezone

logging.basicConfig(level=logging.INFO)  # Configurar el nivel de log


def translate_to_spanish(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='es')
    return translation.text


def get_cities_with_timezones():
    cities = []
    for tz in pytz.common_timezones:
        if tz.startswith('Etc/'):  # Filtro para excluir tz que comiencen con 'Etc/'
            continue

        if '/' not in tz:  # Filtrar regiones y abreviaturas
            continue

        city = tz.split('/')[-1].replace('_', ' ')
        offset_seconds = pytz.timezone(tz).utcoffset(pytz.datetime.datetime.now()).total_seconds()
        offset_hours = int(offset_seconds // 3600)  # Convert to integer
        offset_minutes = int((offset_seconds % 3600) // 60)  # Get minutes from remaining seconds
        offset_sign = '+' if offset_hours >= 0 else '-'  # Determine the sign based on offset hours
        offset_string = "{0}{1:02d}:{2:02d}".format(offset_sign, abs(offset_hours), abs(offset_minutes))  # Format offset as ±HH:MM
        gmt_offset = "GMT " + offset_string

        country_and_continent = get_country_and_continent_from_timezone(tz)
        if country_and_continent is None:
            logging.warning(f"Country and Continent not found for timezone: {tz}")
            continue

        country = country_and_continent['country']
        continent = country_and_continent['continent']

        extra_info = {
            "utcMainCode": tz,
            "gmtOffset": gmt_offset,
            "offset": offset_hours
        }
        extra_info_json = json.dumps(extra_info)

        language_en = f"{continent} - {country} ({city})"
        name = translate_to_spanish(language_en)
        language_en += f" (GMT {offset_string})"
        name += f" (GMT {offset_string})"

        city_info = {
            'name': name,
            'language_en': language_en,
            'language_es': name,
            'language_es_es': name,
            'extras': extra_info_json,
            'description': tz,
            'gmt_offset': gmt_offset,
            'offset': offset_hours
        }
        cities.append(city_info)

    return cities


# Example usage:
all_cities = get_cities_with_timezones()

# Sort cities based on offset in descending order
all_cities.sort(key=lambda x: x['offset'], reverse=True)

# Export results to CSV file
filename = "timezone_results.csv"
fields = ['name', 'language_en', 'language_es', 'language_es_es', 'extras', 'description', 'gmt_offset', 'offset']
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(all_cities)

print("Results exported to", filename)
