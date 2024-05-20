import cmd

class mycmd(cmd.Cmd):
    prompt = ">> "

    def do_sum(self, args):
        nums = [int(num) for num in args]
        print(f"Sum: {sum(nums)}")

    def preloop(self):
        print("type sum then space followed by any group of numbers")

if __name__ == "__main__":
    mycmd().cmdloop()
