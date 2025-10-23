import statistics


def average_raiting(data):
    """Подсчет среднего рейтинга брэндов"""
    brands = {}
    for i in data:
        brand = i['brand']
        rating = float(i['rating'])
        brands.setdefault(brand, []).append(rating)

    brands_result = []
    for brand, rating in brands.items():
        avg_rating = statistics.mean(rating)
        brands_result.append({'brand': brand, 'rating': round(avg_rating, 2)})

    sorted_brands_rating = sorted(
        brands_result,
        key=lambda val: val['rating'],
        reverse=True
        )
    return sorted_brands_rating
