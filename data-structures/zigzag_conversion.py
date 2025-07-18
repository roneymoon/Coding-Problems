def zigziag(s, numRows):
    if(len(s) == 0  and numRows == 1):
        return s
    rows = [""] * numRows
    curr_row = 0
    going_down = False
    for char in s:
        rows[curr_row] += char
        if(curr_row == 0 or curr_row == numRows - 1):
            going_down = not going_down
        curr_row += 1 if going_down else -1
    return "".join(rows)

print(zigziag("PAYPALISHIRING", 3))

            