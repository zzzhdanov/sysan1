import numpy as np

def kendell_calculate(values):
    rank = [[0 for i in range(len(values))] for _ in range(len(values[0]))]
    rank_me = [[len(values[0]) - j for _ in range(len(values))] for j in range(len(values[0]))]
    items = sorted(values[0])

    for i in range(len(values)):
        for j in range(len(values[i])):
            rank[j][i] = len(values[i]) - values[i].index(items[j])

    rank = np.array(rank)
    rank_me = np.array(rank_me)

    d_rank_me = ((rank_me.sum(axis=-1) - rank_me.sum(axis=-1).mean())**2).sum() / (len(values[0]) - 1)
    d_rank_m =  ((rank.sum(axis=-1) - rank.sum(axis=-1).mean())**2).sum() / (len(values[0]) - 1)

    print(d_rank_m)
    print(d_rank_me)

    return d_rank_m / d_rank_me

def main():
    val_1 = ["O1","O2","O3"]
    val_2 = ["O1","O3","O2"]
    val_3 = ["O1","O3","O2"] 
    out = [val_1, val_2, val_3]
    res = kendell_calculate(out)
    print(res)

if __name__ == "__main__":
    main()
