import os, requests, json

GPS_TAGS = {
    0x0001: 'GPSLatitudeRef', 0x0002: 'GPSLatitude',
    0x0003: 'GPSLongitudeRef', 0x0004: 'GPSLongitude',
    0x0005: 'GPSAltitudeRef', 0x0006: 'GPSAltitude',
    0x0007: 'GPSTimeStamp', 0x0008: 'GPSSatellites',
    0x0009: 'GPSStatus', 0x000a: 'GPSMeasureMode',
    0x000b: 'GPSDOP', 0x000c: 'GPSSpeedRef',
    0x000d: 'GPSSpeed', 0x000e: 'GPSTrackRef',
    0x000f: 'GPSTrack', 0x0010: 'GPSImgDirectionRef',
    0x0011: 'GPSImgDirection', 0x0012: 'GPSMapDatum',
    0x0013: 'GPSDestLatitudeRef', 0x0014: 'GPSDestLatitude',
    0x0015: 'GPSDestLongitudeRef', 0x0016: 'GPSDestLongitude',
    0x0017: 'GPSDestBearingRef', 0x0018: 'GPSDestBearing',
    0x0019: 'GPSDestDistanceRef', 0x001a: 'GPSDestDistance',
    0x001d: 'GPSDateStamp', 0x001e: 'GPSDifferential',
}

def exif_metadados(file):
    file.seek(20)
    
    número = int.from_bytes(file.read(2), byteorder='big')

    informaçoes = {}
    for _ in range(número):
        id = int.from_bytes(file.read(2), byteorder='big')
        tipo = int.from_bytes(file.read(2), byteorder='big')
        contador = int.from_bytes(file.read(4), byteorder='big')

        if tipo == 2:  
            try:
                value = file.read(contador).decode('utf-8')
            except UnicodeDecodeError:
                value = repr(file.read(contador))
        else:
            value = int.from_bytes(file.read(4), byteorder='big')

        nome = GPS_TAGS.get(id)
        if nome:
            informaçoes[nome] = value

    return informaçoes

def gps_coordenadas(metadata_info):
    gps_longitude = metadata_info.get('GPSLongitude')
    gps_latitude = metadata_info.get('GPSLatitude')
    
    if gps_latitude is not None and gps_longitude is not None:
        latitude = gps_latitude / 1000000
        longitude = gps_longitude / 1000000

        return latitude, longitude
    else:
        return None, None

def main():
    diretorio = input('Digite o nome do diretório: ')

    arqs = os.listdir(diretorio)
    for n in arqs:
        with open(os.path.join(diretorio, n), 'rb') as f:
            inico = f.read(4)
            if inico[:2] == b'\xff\xd8' and inico[2:] == b'\xff\xe1':
                metadata_info = exif_metadados(f)

                print(f'{n}:')
                print('Largura:', metadata_info.get('ImageWidth'))
                print('Altura:', metadata_info.get('ImageHeight'))
                print('Fabricante da câmera:', metadata_info.get('Make'))
                print('Data/hora da foto:', metadata_info.get('DateTimeOriginal'))
                latitude, longitude = gps_coordenadas(metadata_info)
                if latitude is not None and longitude is not None:
                    print('Latitude:', latitude)
                    print('Longitude:', longitude)
                else:
                    print('Coordenadas indisponíveis.')
    coordenadas = set()
    for n in arqs:
        with open(os.path.join(diretorio, n), 'rb') as f:
            metadata_info = exif_metadados(f)
            latitude, longitude = gps_coordenadas(metadata_info)
            if latitude is not None and longitude is not None:
                coordenadas.add((latitude, longitude))

    for p in coordenadas:
        print(p)

if __name__ == "__main__":
    main()


