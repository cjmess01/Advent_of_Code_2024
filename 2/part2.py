

def passes_tests(numbers):
    last_diff = 0
    for i in range(0, len(numbers) - 1):
        current_diff = numbers[i] - numbers[i+1]
        if(abs(current_diff)> 3 or abs(current_diff) < 1):
            return [i, "Leap error"]
        if((last_diff > 0 and current_diff < 0) or (last_diff < 0 and current_diff > 0) and last_diff != 0 ):
            return [i, "Direction error"]

        last_diff = current_diff

    return [-1, "No error"]


with open("data.txt", "r") as file:
    num_safe = 0
    lines = file.readlines()
    for line in lines:
        strikes_left = 1


        values = [int(obj.strip()) for obj in line.split(' ')]
        print(values)
        ahead= values[:]
        before= values[:]
        current= values[:]
        first = values[:]
        last= values[:]

        passed_trial, reason = passes_tests(values)


        if(passed_trial == -1):
            num_safe += 1
            continue
        else:
            print("Strike 1 taken")
            ahead.pop(passed_trial+1)
            current.pop(passed_trial)
            first.pop(0)
            last.pop(len(values) - 1)
            if(passed_trial != 0):
                before.pop(passed_trial - 1)

        extra_tries = []
        extra_tries.append(passes_tests(ahead)[0])
        extra_tries.append(passes_tests(before)[0])
        extra_tries.append(passes_tests(current)[0])
        extra_tries.append(passes_tests(first)[0])
        extra_tries.append(passes_tests(last)[0])

        print(extra_tries)
        if -1 in extra_tries:
            print("GOOD")
            num_safe += 1
            continue
        print(f"Failed")
        print()

    print(num_safe)




