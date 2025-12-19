puzzleinput = "24-46,124420-259708,584447-720297,51051-105889,6868562486-6868811237,55-116,895924-1049139,307156-347325,372342678-372437056,1791-5048,3172595555-3172666604,866800081-866923262,5446793-5524858,6077-10442,419-818,57540345-57638189,2143479-2274980,683602048-683810921,966-1697,56537997-56591017,1084127-1135835,1-14,2318887654-2318959425,1919154462-1919225485,351261-558210,769193-807148,4355566991-4355749498,809094-894510,11116-39985,9898980197-9898998927,99828221-99856128,9706624-9874989,119-335"
ranges=puzzleinput.split(",")
sum=0
invalids=[]

for i in ranges:
    start=int(i.split("-")[0])
    end=int(i.split("-")[1])
    print(f"-----------------\nRange {i} from {start} to {end}")
    for tj in range(start,end+1):
        strtj=str(tj)
        print(f"    Number {tj} is length {len(strtj)}")
        if len(strtj)%2==0:
            print(f"    half index = {len(strtj)/2}")
            firsthalf=strtj[0:int(len(strtj)/2)]
            secondhalf=strtj[int(len(strtj)/2):len(strtj)]
            print(f"Number has even length, upperhalf {firsthalf}, secondhalf {secondhalf}")
            if firsthalf==secondhalf:
                invalids.append(tj)
                sum+=tj
        else:
            print("    Number has odd length, cannot be symmetrical")

print(f"Invalid Numbers: {invalids}")
print(f"Invalid Sum: {sum}")