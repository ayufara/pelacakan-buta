from distutils.log import warn
from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars

ukuran = Relation()
warna = Relation()
gelap = Relation()

facts(ukuran, ("beruang", "besar"),
              ("gajah", "besar"),
              ("kucing", "kecil"))

facts(warna, ("beruang", "cokelat"),
             ("kucing", "hitam"),
             ("gajah", "kelabu"))

fact(gelap, "hitam")
fact(gelap, "cokelat")

x = var()
y = var()
kecil = run(0, x, ukuran(x, "kecil"))
print("hewan berukuran kecil: ", kecil)

hewan_besar = run(0, x, ukuran(x, "besar"))
print("hewan berukuran besar: ", hewan_besar)

warna_hewan = run(0, x, warna(x, "cokelat"))
print("hewan berwarna cokelat: ", warna_hewan)

q1 = run(0, x, membero(x, warna_hewan), membero(x, hewan_besar))
print("Hewan yang berwarna cokelat dan besar adalah: ", q1)

gelapx = run(0, x, gelap(x, "hitam"))
for hitam in gelapx:
    fact(warna, ("hitam"), hitam)
black = run(0, x, warna(x, "hitam"))

gelaps = run(0, x, gelap(x, "cokelat"))
for cokelat in gelaps:
    fact(warna, ("cokelat"), cokelat)
brown = run(0, x, warna(x, "cokelat"))
print("Hewan berwarna gelap: ", black, brown)

q3 = run(0, x, membero(x, hewan_besar), membero(x, warna_hewan))
print("hewan besar berwarna gelap adalah: ", q3)

jenis = Relation()
facts(jenis, ("beruang", "karnivora"),
              ("kucing", "karnivora"))
jenisx = run(0, x, jenis(x, "karnivora"))
print("Hewan karnivora adalah: ", jenisx)