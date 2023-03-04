from factory import get_session
from cliente import Cliente

session = get_session()

print("="*4, "TUDO", "="*4)
results = session.query(Cliente).all()
for result in results:
    print(result)

print("="*4, "POR ID", "="*4)
result = session.query(Cliente).filter_by(cd_cliente=1)
for r in result:
    print(r)

print("="*4, "POR RENDA", "="*4)
result = session.query(Cliente).filter(Cliente.vl_renda > 1200) \
                               .filter(Cliente.vl_renda <= 1500)
for r in result:
    print(r)

session.close()
