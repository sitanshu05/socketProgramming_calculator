ans = 0
def calc(cmd):
    global ans
    args = cmd.split(' ')
    valid_commands = ['ADD','SUB','MULT', 'DIV','POW']

    if args[0] not in valid_commands:
        return 'INV_CMD'
    
    if 'ANS' in args:
        args[args.index('ANS')] = ans
    
    if args[0] in ['POW','DIV']:
        if len(args) < 3:
            return 'INSUF_ARGS' 
        elif len(args) > 3:
            return 'INV_ARGS'
        else:
            if args[0] == 'POW':
                sol = int(args[1])**int(args[2])
                ans = sol
                return str(sol)
            else:
                if args[2] == '0':
                    return 'DZERO'
                else:
                    sol = int(args[1])/int(args[2])
                    ans = sol
                    return str(sol)
    else:
        operation = args[0]
        if '-n' not in args:
            return 'INV_ARGS'
        n = args.index('-n')
        args_num = int(args[n+1])

        args.pop(0)
        args.pop(n-1)
        args.pop(n-1)

        nums = list(map(float, args))

        if len(args) <= 1 or args_num == 1:
            return 'INSUF_ARGS'
        elif len(args) < args_num:
            return 'INSUF_ARGS'
        elif len(args) > args_num:
            return 'INV_ARGS'
        else:
            if operation == 'ADD':
                ans = sum(nums)
            elif operation == 'SUB':
                sol = nums[0]
                for i in range(1,len(args)):
                    sol = sol - nums[i]
                ans = sol
            elif operation == 'MULT':
                sol = nums[0]
                for i in range(1,len(args)):
                    sol = sol*nums[i]
                ans = sol 
            return(str(ans))
          
                




