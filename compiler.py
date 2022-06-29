out = open('microinstructions', 'w')

def I2N(i):
    r = list('0'*32)
    ls = ['CO', 'CI', 'CE', 'SO', 'SE', 'SD', 'MS', 'MI', 'MO', 'MRO', 'II', 'AO', 'AC', 'AS', 'AA', 'ALA', 'ALO', 'AFO', 'LRA', 'LRB', 'ORA', 'ORB', 'INV', 'OUTV', 'SI', 'SI1', 'HLT', 'INV2', 'OUTV2']
    for e in i:
        r[len(r)-1-ls.index(e)] = '1'
    return int(''.join(r), 2)

data = [I2N(['SI']) for _ in range(2047)]

ins = {
    0x00: [['CO', 'MS'], ['MRO', 'MS', 'CE'], ['MO', 'LRA']],  # LDA
    0x01: [['CO', 'MS'], ['MRO', 'MS', 'CE'], ['MO', 'LRB']],  # LDB
    0x02: [['CO', 'MS'], ['MRO', 'MS', 'CE'], ['ORA', 'MI']],  # STA
    0x03: [['CO', 'MS'], ['MRO', 'MS', 'CE'], ['ORB', 'MI']],  # STB
    0x04: [['AA', 'AO', 'LRA']],  # ADD
    0x05: [['AA', 'AO', 'LRA', 'AC']],  # ADC
    0x06: [['AS', 'AO', 'LRA']],  # SUB

    0x08: [['ALA', 'AO', 'LRA']],  # AND
    0x09: [['ALO', 'AO', 'LRA']],  # OR

    0x0B: [['CO', 'MS'], ['MRO', 'CI']],  # JMP
    0x0C: [['AFO', 'SI1'], ['CO', 'MS'], ['MRO', 'CI']],  # JO

    0x0D: [['SE', 'SD'], ['SO', 'MS'], ['ORA', 'MI']],  # PUSH
    0x0E: [['SO', 'MS'], ['MO', 'LRA', 'SE']],  # POP
    0x0F: [['CO', 'MS'], ['MRO', 'LRA', 'CE']],  # ST,
    0x10: [['INV', 'LRA']],  # INA
    0x11: [['INV', 'LRB']],  # INB
    0x12: [['OUTV', 'ORA']],  # OUTA
    0x13: [['OUTV', 'ORB']],  # OUTB
    0x14: [['INV2', 'LRA']],  # INA2
    0x15: [['INV2', 'LRB']],  # INB2
    0x16: [['OUTV2', 'ORA']],  # OUTA2
    0x17: [['OUTV2', 'ORB']],  # OUTB2
    0x18: [['SE', 'SD'], ['SO', 'MS'], ['ORB', 'MI']],  # BPUSH
    0x19: [['SO', 'MS'], ['MO', 'LRB', 'SE']],  # BPOP
    0x1A: [['CO', 'MS'], ['MRO', 'LRB', 'CE']],  # BST
    0x1B: [['LRA', 'CO']],  # PCA
    0x1C: [['ORA', 'CI']],  # APC
    0x1D: [['CO', 'MS'], ['MRO', 'MS', 'CE'], ['MO', 'CI'], ['MO', 'CI']],  # JRR

    0xFE: [[]],
    0xFF: [['HLT']]
}

# generate basic instruction for each data
for i in range(256):
    data[int(f'{bin(i)[2:].zfill(8)}000', 2)] = I2N(['CO', 'MS'])
    data[int(f'{bin(i)[2:].zfill(8)}001', 2)] = I2N(['CE', 'MRO', 'II'])

# generate for each instruction
for k, v in ins.items():
    for i in range(len(v)):
        data[int(f'{bin(k)[2:].zfill(8)}{bin(i+2)[2:].zfill(3)}', 2)] = I2N(v[i])

out.write(' '.join(map(lambda e: hex(e)[2:].zfill(8), data)))
out.close()