import requests

GAME_ID = 2024030416

url = "https://api.nhle.com/stats/rest/en/shiftcharts"

response = requests.get(
    url,
    params={"cayenneExp": f"gameId={GAME_ID}"},
    timeout=15
)

print(response.status_code)

data = response.json()
shifts = data["data"]

print(type(data))
print(data.keys())
print("Vaihtojen määrä:", len(data["data"]))
print(shifts[0])

barkov_shifts = []

for shift in shifts:
    if shift["lastName"] == "Barkov":
        print("Erä ", shift["period"], " aloitusaika ", shift["startTime"], " lopetusaika ", shift["endTime"])
        barkov_shifts.append(shift)

print(len(barkov_shifts))

def time_to_seconds(min_secs):
    split_times = min_secs.split(":")
    seconds = int(split_times[0]) * 60 + int(split_times[1])
    return seconds

print(time_to_seconds("3:30"))

def game_time_seconds(period, time):
    earlier_periods = (int(period)-1) * 20 * 60 
    return earlier_periods + time_to_seconds(time)

print(game_time_seconds("2", "3:30"))

barkov_shifts_seconds = []

for shift in barkov_shifts:
    period = shift["period"]
    start_time = game_time_seconds(period, shift["startTime"])
    end_time = game_time_seconds(period, shift["endTime"])
    barkov_shifts_seconds.append( {
        "period": period,
        "start_seconds": start_time,
        "end_seconds": end_time
    })

print (barkov_shifts_seconds)
