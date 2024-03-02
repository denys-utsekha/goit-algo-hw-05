import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

with open('text_1.txt', 'r') as file:
    text_1 = file.read()
with open('text_2.txt', 'r') as file:
    text_2 = file.read()


if __name__ == "__main__":
    text_1_real_pattern = "if (previousStep == Math.min(jumpStep"
    text_1_fake_pattern = "Database Systems: Triples Storage and"
    text_2_real_pattern = "Нижче наведено параметри кожної"
    text_2_fake_pattern = "направляємо індекс у middle+1"

    bms_text_1 = timeit.timeit(lambda: boyer_moore_search(text_1,
                                                          text_1_real_pattern), number=3)
    bms_text_1_fake = timeit.timeit(lambda: boyer_moore_search(text_1,
                                                               text_1_fake_pattern), number=3)
    bms_text_2 = timeit.timeit(lambda: boyer_moore_search(text_2,
                                                          text_2_real_pattern), number=3)
    bms_text_2_fake = timeit.timeit(lambda: boyer_moore_search(text_2,
                                                               text_2_fake_pattern), number=3)

    kmp_text_1 = timeit.timeit(lambda: kmp_search(text_1,
                                                  text_1_real_pattern), number=3)
    kmp_text_1_fake = timeit.timeit(lambda: kmp_search(text_1,
                                                       text_1_fake_pattern), number=3)
    kmp_text_2 = timeit.timeit(lambda: kmp_search(text_2,
                                                  text_2_real_pattern), number=3)
    kmp_text_2_fake = timeit.timeit(lambda: kmp_search(text_2,
                                                       text_2_fake_pattern), number=3)

    rks_text_1 = timeit.timeit(lambda: rabin_karp_search(text_1,
                                                         text_1_real_pattern), number=3)
    rks_text_1_fake = timeit.timeit(lambda: rabin_karp_search(text_1,
                                                              text_1_fake_pattern), number=3)
    rks_text_2 = timeit.timeit(lambda: rabin_karp_search(text_2,
                                                         text_2_real_pattern), number=3)
    rks_text_2_fake = timeit.timeit(lambda: rabin_karp_search(text_2,
                                                              text_2_fake_pattern), number=3)

    print(f"| {'Algorithm':<20} | {f'Text 1 (len={len(text_1)})':<20} | {
          'Text 1 fake':<20} | {f'Text 2 (len={len(text_2)})':<20} | {'Text 2 fake':<20} |")
    print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
    print(f"| {'Boyer-Moore':<20} | {bms_text_1:20.5f} | {
          bms_text_1_fake:20.5f} | {bms_text_2:20.5f} | {bms_text_2_fake:20.5f} |")
    print(f"| {'Knuth–Morris–Pratt':<20} | {kmp_text_1:20.5f} | {
          kmp_text_1_fake:20.5f} | {kmp_text_2:20.5f} | {kmp_text_2_fake:20.5f} |")
    print(f"| {'Rabin-Karp':<20} | {rks_text_1:20.5f} | {
          rks_text_1_fake:20.5f} | {rks_text_2:20.5f} | {rks_text_2_fake:20.5f} |")
