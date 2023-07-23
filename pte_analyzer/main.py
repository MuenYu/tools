overall = 66

data = {
    "DI RL SST SWT WE": 62,
    "RA RS WFD": 73,
    "SST SWT WE": 58,
    "WFD FIB-RW": 68,
    "DI RL": 79,
    "RA RS ASQ": 82,
    "RA RL SWT": 67,
    "SST WFD RO FIB-RW FIB-R": 53,
}
weakness = {}

if overall == 0:
    overall = int(input("enter your pte score: "))
for k, v in data.items():
    if v == 0:
        data[k] = int(input("enter value for {}: ".format(k)))
    if v <= overall:
        fields = k.split(' ')
        for field in fields:
            if field in weakness:
                weakness[field] += 1
            else:
                weakness[field] = 1

result = {k: v for k, v in sorted(weakness.items(), key=lambda item: item[1], reverse=True)}
for k, v in result.items():
    if v > 1:
        print(k, v)
