Pytest ,Python programları için bir test çerçevesidir. Yazılım projelerinde testlerin yazılması ve çalıştırılması için kullanılır.
Pytest, basit test senaryolarından karmaşık test süitlerine kadar çeşitli testleri destekler.
Decoratorler, pytest test çerçevesini daha esnek ve güçlü kılan özelliklerden sadece birkaç tanesidir.
Her decoratorün belirli bir kullanım amacı vardır ve belirli durumlar için test yazımını kolaylaştırmak için tasarlanmıştır.


1-@pytest.fixture: Fixture'lar, testlerin öncesi veya sonrasında çalıştırılmak üzere tanımlanan ve tekrar kullanılabilir yapılar sağlayan fonksiyonlardır. Bu decorator ile bir fonksiyonun bir fixture olduğu belirtilir.

2-@pytest.mark.parametrize: Bir test fonksiyonunu farklı parametre setleriyle birden fazla kez çalıştırmak için kullanılır. Her parametre seti için ayrı bir test geçmişi oluşturur.

3-@pytest.mark.skip: Bir test fonksiyonunun çalıştırılmasını geçici olarak engellemek için kullanılır. Test, belirtilen nedenle geçici olarak atlanır.

4-@pytest.mark.skipif: Belirli bir koşul sağlandığında bir test fonksiyonunun çalıştırılmasını engeller. Koşulun doğru olması durumunda test atlanır.

5-@pytest.mark.xfail: Bir testin beklenen bir hata ile sonuçlanmasını işaretlemek için kullanılır. Test başarısız olsa bile sonuç geçerli olarak kabul edilir.

6-@pytest.mark.timeout: Bir testin belirli bir sürede tamamlanmasını beklemek için kullanılır. Belirtilen süreden daha uzun süren testler başarısız olur.

