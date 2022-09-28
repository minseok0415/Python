class human:
    def __init__(self, height, age):
        self.height = height # 멤버변수
        self.age = age # 멤버변수

    def how_old(self): # 메소드
        print(self.age, "살입니다.")

    def how_tall(self): # 메소드
        print(self.height, "cm 입니다.")

minseok = human(168, 17) # 인스턴스 생성
someone = human(180, 22) # 인스턴스 생성

minseok.how_old()
human.how_old(minseok)

someone.how_tall()

print(minseok.height)
