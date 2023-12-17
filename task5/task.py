import json
import numpy as np

def extract_matrix(j_string):
    c = exctract_clusters(j_string)
    n = sum(len(cluster) for cluster in c)
    m = np.ones((n, n), dtype=int)
    worse = []
    for cluster in c:
        for worse_elem in worse:
            for elem in cluster:
                m[elem - 1][worse_elem - 1] = 0
        worse.extend(cluster)
    return m

def exctract_clusters(j_string):
    с_list = json.loads(j_string)
    c = []
    for item in с_list:
        if isinstance(item, list):
            c.append(item)
        else:
            c.append([item])
    return c

def fetch_cls(matrix, est1, est2):
    c = {}
    exclude = set()

    rows, cols = matrix.shape
    for row in range(rows):
        if row + 1 in exclude:
            continue
        c[row + 1] = [row + 1]
        for col in range(row + 1, cols):
            if matrix[row][col] == 0:
                c[row + 1].append(col + 1)
                exclude.add(col + 1)

    out = []
    for k in c:
        if not out:
            out.append(c[k])
            continue

        for i, elem in enumerate(out):
            if (
                np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1])
                and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1])
            ):
                out[i].extend(c[k])
                break

            if (
                np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1])
                or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1])
            ):
                out = out[:i] + c[k] + out[i:]
                break
        out.append(c[k])
    definitive = [r[0] if len(r) == 1 else r for r in out]
    return str(definitive)

def _and(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)


def _or(matrix1, matrix2):
    return np.maximum(matrix1, matrix2)



def calculate(str_1, str_2):
    mx1 = extract_matrix(str_1)
    mx2 = extract_matrix(str_2)

    mx_and = _and(mx1, mx2)
    mx_and_t = _and(np.transpose(mx1), np.transpose(mx2))

    mx_or = _or(mx_and, mx_and_t)
    clusters = fetch_cls(mx_or, mx1, mx2)
    return clusters


if __name__ == "__main__":
    j_str_1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    j_str_2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    out = calculate(j_str_1, j_str_2)
    print(out)
