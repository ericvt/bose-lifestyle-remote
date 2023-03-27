import serial

serial_port = serial.Serial('/dev/tty.usbserial', baudrate=1200, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

INIT = b'TAP\r'
REMOTE = b'aE'
codes = {
    'on': b'@@',
    'off': b'@@',
    'volup': b'A@',
    'rev': b'BA',
    'play': b'CC',
    'fwd': b'DD',
    'voldown': b'EE',
    'nextdisc': b'FF',
    'video1': b'GG',
    'video2': b'HH',
    'aux': b'II',
    'cd': b'JJ',
    'fm': b'KK',
    'tape': b'LL',
    'stop': b'MM',
    'mute': b'NN',
    'muteall': b'OO',
    'random': b'PP',
    'survolup': b'QQ',
    'survoldown': b'RR',
    'surround': b'SS',
    'stereo_center': b'TT',
    'stereo': b'UU',
    'preset_0': b'VV',
    'preset_1': b'WW',
    'preset_2': b'XX',
    'preset_3': b'YY',
    'preset_4': b'ZZ',
    'preset_5': b'[[',
    'preset_6': b'\@'
}

def write_data(str, callback):
    count = 0
    def write(data, fn):
        nonlocal count
        print('write:', data.decode('utf-8'))
        serial_port.write(data)
        count += 1
        if count < len(str):
            setTimeout(lambda: write(str[count].encode('utf-8'), fn), 50)
        else:
            fn()

    write(str[count].encode('utf-8'), callback)

print(sys.argv[1])
serial_port.open()

def on_data_received(data):
    print('data received: ' + data.decode('utf-8'))

serial_port.reset_input_buffer()
serial_port.reset_output_buffer()
serial_port.write(INIT)

code = codes[sys.argv[1]]
write_data(REMOTE + code + b'axxx', lambda: print("AND DONE"))

serial_port.close()
