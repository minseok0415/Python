# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린" # 유닛 이름
hp = 40 # 체력
damage = 5 # 공격력

print(f"\n{name} 유닛이 생성되었습니다. ")
print(f"체력 {hp}, 공격력 {damage} ")

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크" # 유닛 이름
tank_hp = 150 # 체력
tank_damage = 35 # 공격력

print(f"\n{tank_name} 유닛이 생성되었습니다. ")
print(f"체력 {tank_hp}, 공격력 {tank_damage} ")

def attack(name, location, damage):
    print(f"\n{name} : {location} 방향으로 적군을 공격합니다. 공격력 {damage}")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
print()