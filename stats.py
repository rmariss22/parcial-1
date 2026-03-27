class stats:
    @staticmethod
    def sum(a):
        total= 0
        for x in a:
            total += x
        return total
    @staticmethod
    def average(a):
        total= stats.sum(a)
        return total/len(a)
    
def main():
    grandes = [80, 75, 90, 60, 95] 

    total = stats.sum(grandes)
    avg = stats.average(grandes)

    print("sum:", total)
    print("average:", avg)

if __name__ == "__main__": 
  main()
