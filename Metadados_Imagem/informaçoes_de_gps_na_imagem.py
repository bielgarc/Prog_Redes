import os
import struct

# Solicita ao usuário o nome da imagem ou o caminho da onde ela se encontra
imagem = input('Digite o nome da imagem ou o caminho completo: ')

# Verifica se o caminho da imagem é válido
if not os.path.exists(imagem):
    print('O caminho da fornecido da imagem é inválido')
else:
    # Abre o arquivo de imagem 
    with open(imagem, 'rb') as imagem_file:
        exif_data = imagem_file.read(20)

    # Dicionário para armazenar as informações de GPS
    informaçoes_gps = {}

    # Dicionário das Tags do GPS
    tag_valores = {
        0x0001: 'GPSLatitudeRef',               0x0002: 'GPSLatitude',
        0x0003: 'GPSLongitudeRef',              0x0004: 'GPSLongitude',
        0x0005: 'GPSAltitudeRef',               0x0006: 'GPSAltitude',
        0x0007: 'GPSTimeStamp',                 0x0008: 'GPSSatellites',
        0x0009: 'GPSStatus',                    0x000a: 'GPSMeasureMode',
        0x000b: 'GPSDOP',                       0x000c: 'GPSSpeedRef',
        0x000d: 'GPSSpeed',                     0x000e: 'GPSTrackRef',
        0x000f: 'GPSTrack',                     0x0010: 'GPSImgDirectionRef',
        0x0011: 'GPSImgDirection',              0x0012: 'GPSMapDatum',
        0x0013: 'GPSDestLatitudeRef',           0x0014: 'GPSDestLatitude',
        0x0015: 'GPSDestLongitudeRef',          0x0016: 'GPSDestLongitude',
        0x0017: 'GPSDestBearingRef',            0x0018: 'GPSDestBearing',
        0x0019: 'GPSDestDistanceRef',           0x001a: 'GPSDestDistance',
        0x001d: 'GPSDateStamp',                 0x001e: 'GPSDifferential',
    }

    # Percorre o dicionário de Tags e seus valores
    for id_tag, nome in tag_valores.items():
        if id_tag in struct.unpack('H' * 10, exif_data[0:20]):
            # Encontra a Tag ID
            id = exif_data.find(struct.pack('H', id_tag))
            if id != -1:
                value = exif_data[id + 12:id + 20].strip(b'\x00').decode('utf-8')
                informaçoes_gps[nome] = value

    # Imprime as informações de GPS
    print('Informações de GPS:')
    for key, value in informaçoes_gps.items():
        print(f'{key}: {value}')

