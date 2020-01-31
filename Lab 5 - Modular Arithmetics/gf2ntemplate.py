# 50.042 FCS Lab 5 Modular Arithmetics
# Year 2019

"""
    Sumedha 1002876
"""
import copy

def deg(coeffs):
    result = 0
    for count, i in enumerate(coeffs):
        if i != 0:
            result = count
    return result

class Polynomial2:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def add(self, p2):
        poly1 = self.coeffs
        poly2 = p2.coeffs
        # the length of coeffs list is different in p1 and p2, so need to make it the same length
        len1 = len(poly1)
        len2 = len(poly2)
        # print('p1:', len1)
        # print('p2:', poly2)

        # find the length difference
        diff = abs(len1 - len2)
        if len1 > len2:
            for i in range(diff):
                poly2.append(0)

        else:
            for i in range(diff):
                poly1.append(0)

        result = []
        # Consider all pairs in (poly1[i], poly2[j)
        # print(poly1)
        for counter, value in enumerate(poly1):
            result.append(poly2[counter] ^ value)
            # print(result)

        return result

    def sub(self, p2):
        poly1 = self.coeffs
        poly2 = p2.coeffs
        len1 = len(poly1)
        len2 = len(poly2)

        # find the length difference
        diff = abs(len1 - len2)
        if len1 > len2:
            for i in range(diff):
                poly2.append(0)

        else:
            for i in range(diff):
                poly1.append(0)

        result = []
        # Consider all pairs in (poly1[i], poly2[j)
        for counter, value in enumerate(poly1):
            result.append(poly2[counter] ^ value)

        return result

    def mul(self, p2, modp=None):
        poly1 = self.coeffs
        poly2 = p2.coeffs  # poly4
        # modp = modp.coeffs
        result = Polynomial2([0])

        for counter, value in enumerate(poly1):
            if value == 1:
                partial = Polynomial2([0] * counter + poly2)
                # print("partial:", partial)
                # partial: x^8+x^5+x^4+x^3+x^2
                # print("partial:", partial.coeffs)
                # partial.coeffs = [0, 0, 1, 1, 1, 1, 0, 0, 1]
                if modp is not None:
                    while len(partial.coeffs) >= len(modp.coeffs):
                        diff = len(partial.coeffs) - len(modp.coeffs)
                        partial_ls = partial.sub(Polynomial2([0] * diff + modp.coeffs))

                        iszero = 0
                        for counter2, value2 in enumerate(partial.coeffs):
                            iszero = counter2 if value2 == 1 else iszero
                            # if value2 == 1:
                            #     iszero = counter2
                            # else:
                            #     iszero
                        partial.coeffs = partial.coeffs[:iszero+1]
                result = result.add(partial.coeffs)
        return result

    def div(self, p2):
        q = Polynomial2([0])
        # deepcopy so wont affect original value
        r = copy.deepcopy(self)  # a = r
        b = copy.deepcopy(p2)
        c = b.coeffs[-1]
        d = deg(b.coeffs)
        degr = deg(r.coeffs)

        # Euclidean Division
        while degr >= d:
            s = [0] * degr
            s[degr - d] = r.coeffs[-1] and c
            s = Polynomial2(s)
            q = q.add(s)
            r = r.sub(s.mul(b))
            iszero = 0
            for counter, value in enumerate(r.coeffs):
                iszero = counter if value == 1 else iszero
            r.coeffs = r.coeffs[:iszero + 1]

        return q, r

    def __str__(self):
        coeffslist = self.coeffs
        poly = ""

        for counter, value in enumerate(coeffslist):
            if value == 1:
                poly = "x^" + str(counter) + "+" + poly

        poly_inv = poly[:-1]
        return poly_inv

    def getInt(p):
        output = 0
        for counter, value in enumerate(p.coeffs):
            output += value * (2 ** counter)
        return output


class GF2N:
    affinemat = [[1, 0, 0, 0, 1, 1, 1, 1],
                 [1, 1, 0, 0, 0, 1, 1, 1],
                 [1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 1, 1]]

    def __init__(self, x, n=8, ip=Polynomial2([1, 1, 0, 1, 1, 0, 0, 0, 1])):
        self.x = x
        self.n = n
        self.ip = ip

    def add(self, g2):
        return self.x ^ g2.x  # XOR

    def sub(self, g2):
        return self.x ^ g2.x

    def mul(self, g2):
        g = copy.deepcopy(self.g2)
        g = Polynomial2().mul(g2.getPolynomial2(), g.ip)
        return g

    def div(self, g2):
        g = copy.deepcopy(self.g2)
        quotient, remainder = g.Polynomial2().div(g.Polynomial2())
        return (quotient, remainder)

    def getPolynomial2(self):
        output = []
        x = copy.deepcopy(self.x)
        # print(x)

        while x > 1:
            output.append(x % 2)
            x = x // 2
        output.append(x)
        return Polynomial2(output)

    def __str__(self):
        return str(self.x)

    def getInt(self):
        return self.x

    def mulInv(self):
        pass

    def affineMap(self):
        pass


print('\nTest 1')
print('======')
print('p1=x^5+x^2+x')
print('p2=x^3+x^2+1')
p1 = Polynomial2([0, 1, 1, 0, 0, 1])
p2 = Polynomial2([1, 0, 1, 1])
p3 = p1.add(p2)
print('p3= p1+p2 = ', p3)  # [1,1,0,1,0,1]

print('\nTest 2')
print('======')
print('p4=x^7+x^4+x^3+x^2+x')
print('modp=x^8+x^7+x^5+x^4+1')
p4 = Polynomial2([0, 1, 1, 1, 1, 0, 0, 1])
modp = Polynomial2([1, 0, 0, 0, 1, 1, 0, 1, 1])
p5 = p1.mul(p4, modp)
print('p5=p1*p4 mod (modp)=', p5)

print('\nTest 3')
print('======')
print('p6=x^12+x^7+x^2')
print('p7=x^8+x^4+x^3+x+1')
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print('q for p6/p7=',p8q)
print('r for p6/p7=',p8r)

####
print('\nTest 4')
print('======')
g1=GF2N(100)
g2=GF2N(5)
print('g1 = ',g1.getPolynomial2())
print('g2 = ',g2.getPolynomial2())
g3=g1.add(g2)
print('g1+g2 = ',g3)

print('\nTest 5')
print('======')
ip=Polynomial2([1,1,0,0,1])
print('irreducible polynomial',ip)
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print('g4 = ',g4.getPolynomial2())
print('g5 = ',g5.getPolynomial2())
g6=g4.mul(g5)
print('g4 x g5 = ',g6.p)

print('\nTest 6')
print('======')
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print('g7 = ',g7.getPolynomial2())
print('g8 = ',g8.getPolynomial2())
q,r=g7.div(g8)
print('g7/g8 =')
print('q = ',q.getPolynomial2())
print('r = ',r.getPolynomial2())

print ('\nTest 7')
print ('======')
ip=Polynomial2([1,1,0,0,1])
print ('irreducible polynomial',ip)
g9=GF2N(0b101,4,ip)
print ('g9 = ',g9.getPolynomial2())
print ('inverse of g9 =',g9.mulInv().getPolynomial2())

print ('\nTest 8')
print ('======')
ip=Polynomial2([1,1,0,1,1,0,0,0,1])
print ('irreducible polynomial',ip)
g10=GF2N(0xc2,8,ip)
print ('g10 = 0xc2')
g11=g10.mulInv()
print ('inverse of g10 = g11 =', hex(g11.getInt()))
g12=g11.affineMap()
print ('affine map of g11 =',hex(g12.getInt()))