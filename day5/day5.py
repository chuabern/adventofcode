import numpy as np

with open("day5_input.txt", "r") as f:
    all_seats = list(f.read().split('\n'))

def split_rows(seat_list):
    half_point = int(len(seat_list)/2)
    first_half = seat_list[0:half_point]
    second_half = seat_list[half_point:]
    return (first_half, second_half)

def get_seat_ids(all_seats):
    seat_ids = []

    for rows in all_seats:
        row_list = list(range(0,128))
        #Row
        for i in range(7):
            first_half, second_half = split_rows(row_list)
            if rows[i] == 'F':
                row = first_half
            elif rows[i] == 'B':
                row = second_half
            row_list = row
        row_number = row_list[0]

        #Column
        column_list = list(range(0,8))
        for i in range(3):
            first_half, second_half = split_rows(column_list)
            if rows[-3:][i] == 'L':
                column = first_half
            elif rows[-3:][i] == 'R':
                column = second_half
            column_list = column
        column_number = column_list[0]

        seat_id = row_number*8 + column_number
        seat_ids.append(seat_id)

    return(seat_ids)

seat_ids = sorted(get_seat_ids(all_seats))


actual_seat = 0

while actual_seat == 0:
    for seat in seat_ids:
        if seat == seat_ids[0] or seat == seat_ids[-1]: #remove first and last seat
            continue
        if seat-1 not in seat_ids and seat+1 in seat_ids:
            lower_seat = seat
            print(lower_seat)
        if seat+1 not in seat_ids and seat-1 in seat_ids:
            upper_seat = seat
            print(upper_seat)
    actual_seat = int(lower_seat+upper_seat)/2

print(actual_seat)


