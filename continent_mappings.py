
import pytz
import pycountry

# Mapping of country codes to their respective continents

country_to_continent = {'AD': 'Europe', 'AL': 'Europe', 'AT': 'Europe', 'BA': 'Europe', 'BE': 'Europe', 'BG': 'Europe', 'BY': 'Europe', 'CH': 'Europe', 'CZ': 'Europe', 'DE': 'Europe', 'DK': 'Europe', 'EE': 'Europe', 'ES': 'Europe', 'FI': 'Europe', 'FO': 'Europe', 'FR': 'Europe', 'GB': 'Europe', 'GG': 'Europe', 'GI': 'Europe', 'GR': 'Europe', 'HR': 'Europe', 'HU': 'Europe', 'IE': 'Europe', 'IM': 'Europe', 'IS': 'Europe', 'IT': 'Europe', 'JE': 'Europe', 'LI': 'Europe', 'LT': 'Europe', 'LU': 'Europe', 'LV': 'Europe', 'MC': 'Europe', 'MD': 'Europe', 'ME': 'Europe', 'MK': 'Europe', 'MT': 'Europe', 'NL': 'Europe', 'NO': 'Europe', 'PL': 'Europe', 'PT': 'Europe', 'RO': 'Europe', 'RS': 'Europe', 'RU': 'Europe', 'SE': 'Europe', 'SI': 'Europe', 'SJ': 'Europe', 'SK': 'Europe', 'SM': 'Europe', 'UA': 'Europe', 'VA': 'Europe', 'XK': 'Europe', 'AE': 'Middle East', 'AF': 'Asia', 'AM': 'Middle East', 'AZ': 'Middle East', 'BD': 'Asia', 'BH': 'Middle East', 'BN': 'Asia', 'BT': 'Asia', 'CN': 'Asia', 'CY': 'Middle East', 'GE': 'Middle East', 'ID': 'Asia', 'IL': 'Middle East', 'IN': 'Asia', 'IQ': 'Middle East', 'IR': 'Middle East', 'JO': 'Middle East', 'JP': 'Asia', 'KG': 'Central Asia', 'KH': 'Asia', 'KP': 'Asia', 'KR': 'Asia', 'KW': 'Middle East', 'KZ': 'Central Asia', 'LA': 'Asia', 'LB': 'Middle East', 'LK': 'Asia', 'MM': 'Asia', 'MN': 'Asia', 'MO': 'Asia', 'MV': 'Asia', 'MY': 'Asia', 'NP': 'Asia', 'OM': 'Middle East', 'PH': 'Asia', 'PK': 'Asia', 'PS': 'Asia', 'QA': 'Middle East', 'SA': 'Middle East', 'SG': 'Asia', 'SY': 'Middle East', 'TH': 'Asia', 'TJ': 'Central Asia', 'TL': 'Asia', 'TM': 'Central Asia', 'TR': 'Middle East', 'TW': 'Asia', 'UZ': 'Central Asia', 'VN': 'Asia', 'YE': 'Middle East', 'DZ': 'Africa', 'AO': 'Africa', 'BJ': 'Africa', 'BW': 'Africa', 'BF': 'Africa', 'BI': 'Africa', 'CV': 'Africa', 'CM': 'Africa', 'CF': 'Africa', 'TD': 'Africa', 'KM': 'Africa', 'CD': 'Africa', 'CG': 'Africa', 'DJ': 'Africa', 'EG': 'Africa', 'GQ': 'Africa', 'ER': 'Africa', 'SZ': 'Africa', 'ET': 'Africa', 'GA': 'Africa', 'GM': 'Africa', 'GH': 'Africa', 'GN': 'Africa', 'GW': 'Africa', 'CI': 'Africa', 'KE': 'Africa', 'LS': 'Africa', 'LR': 'Africa', 'LY': 'Africa', 'MG': 'Africa', 'MW': 'Africa', 'ML': 'Africa', 'MR': 'Africa', 'MU': 'Africa', 'MA': 'Africa', 'MZ': 'Africa', 'NA': 'Africa', 'NE': 'Africa', 'NG': 'Africa', 'RW': 'Africa', 'ST': 'Africa', 'SN': 'Africa', 'SC': 'Africa', 'SL': 'Africa', 'SO': 'Africa', 'ZA': 'Africa', 'SS': 'Africa', 'SD': 'Africa', 'TZ': 'Africa', 'TG': 'Africa', 'TN': 'Africa', 'UG': 'Africa', 'EH': 'Africa', 'ZM': 'Africa', 'ZW': 'Africa', 'AG': 'Caribbean', 'BS': 'Caribbean', 'BB': 'Caribbean', 'BZ': 'North America', 'CA': 'North America', 'CR': 'North America', 'CU': 'Caribbean', 'DM': 'Caribbean', 'DO': 'Caribbean', 'SV': 'North America', 'GD': 'Caribbean', 'GT': 'North America', 'HT': 'Caribbean', 'HN': 'North America', 'JM': 'Caribbean', 'MX': 'North America', 'NI': 'North America', 'PA': 'North America', 'KN': 'Caribbean', 'LC': 'Caribbean', 'PM': 'North America', 'VC': 'Caribbean', 'TT': 'Caribbean', 'US': 'North America', 'AR': 'South America', 'BO': 'South America', 'BR': 'South America', 'CL': 'South America', 'CO': 'South America', 'EC': 'South America', 'GY': 'South America', 'PY': 'South America', 'PE': 'South America', 'SR': 'South America', 'UY': 'South America', 'VE': 'South America', 'AS': 'Oceania', 'AU': 'Oceania', 'CK': 'Oceania', 'FJ': 'Oceania', 'PF': 'Oceania', 'GU': 'Oceania', 'KI': 'Oceania', 'MH': 'Oceania', 'FM': 'Oceania', 'NR': 'Oceania', 'NC': 'Oceania', 'NZ': 'Oceania', 'NU': 'Oceania', 'NF': 'Oceania', 'MP': 'Oceania', 'PW': 'Oceania', 'PG': 'Oceania', 'PN': 'Oceania', 'WS': 'Oceania', 'SB': 'Oceania', 'TK': 'Oceania', 'TO': 'Oceania', 'TV': 'Oceania', 'UM': 'Oceania', 'VU': 'Oceania', 'WF': 'Oceania', 'AQ': 'Antarctica', 'AI': 'Caribbean', 'AW': 'Caribbean', 'BQ': 'Caribbean', 'VG': 'Caribbean', 'KY': 'Caribbean', 'CW': 'Caribbean', 'GP': 'Caribbean', 'MQ': 'Caribbean', 'MS': 'Caribbean', 'PR': 'Caribbean', 'BL': 'Caribbean', 'MF': 'Caribbean', 'SX': 'Caribbean', 'TC': 'Caribbean', 'VI': 'Caribbean'}

def get_country_and_continent_from_timezone(timezone):
    special_timezones = {
        'US/Alaska': ('United States', 'North America'),
        'US/Arizona': ('United States', 'North America'),
        'US/Central': ('United States', 'North America'),
        'US/Eastern': ('United States', 'North America'),
        'US/Hawaii': ('United States', 'North America'),
        'US/Mountain': ('United States', 'North America'),
        'US/Pacific': ('United States', 'North America'),
        'Canada/Atlantic': ('Canada', 'North America'),
        'Canada/Central': ('Canada', 'North America'),
        'Canada/Eastern': ('Canada', 'North America'),
        'Canada/Mountain': ('Canada', 'North America'),
        'Canada/Newfoundland': ('Canada', 'North America'),
        'Canada/Pacific': ('Canada', 'North America')
    }
    
    # If the timezone is one of the special cases, return the mapped country and continent
    if timezone in special_timezones:
        country_name, continent = special_timezones[timezone]
        return {
            'country': country_name,
            'continent': continent
        }

    for country, timezones in pytz.country_timezones.items():
        if timezone in timezones:
            # Get country using ISO code
            country_info = pycountry.countries.get(alpha_2=country)
            country_name = country_info.name

            # Get continent using the mapping
            continent = country_to_continent.get(country, "Unknown")

            return {
                'country': country_name,
                'continent': continent
            }
    return None

