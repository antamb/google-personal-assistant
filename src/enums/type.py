from enum import Enum


class Type(Enum):
    OTHER = 1
    EVENT = 2
    PERSON = 3
    UNKNOWN = 4
    LOCATION = 5
    WORK_OF_ART = 6
    ORGANIZATION = 7
    CONSUMER_GOOD = 8


entities_type = {
    Type.EVENT: 'Event',
    Type.PERSON: 'Person',
    Type.UNKNOWN: 'Unknown',
    Type.OTHER: 'Other types',
    Type.LOCATION: 'Location',
    Type.WORK_OF_ART: '	Work of art',
    Type.ORGANIZATION: 'Organization',
    Type.CONSUMER_GOOD: 'Consumer goods',
}


def get_type_from_value(value):
    value_type = Type.UNKNOWN
    for t in Type:
        if entities_type[t] == value:
            value_type = t
    return value_type
