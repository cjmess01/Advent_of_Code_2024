with open("data.txt", "r") as file:
    num_safe = 0
    lines = file.readlines()
    for line in lines:

        safe = 1
        values = [int(obj.strip()) for obj in line.split(' ')]

        last_diff = 0
        current_diff = 0
        for i in range(0, len(values ) -1):
            current_diff = (values[i] - values[i+1])
            if(abs(current_diff)> 3 or abs(current_diff) < 1):
                safe = 0
                break

            if((last_diff > 0 and current_diff < 0) or (last_diff < 0 and current_diff > 0) and last_diff != 0 ):
                safe = 0
                break
            last_diff = current_diff

        num_safe += safe
        # print(safe)
        print(values)

    print(num_safe)




