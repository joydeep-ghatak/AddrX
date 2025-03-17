import time

from addrx import AddrX

url = "http://0.0.0.0:4400"

address = ["19 canada square, London, uk"]
addr_list = address * 1


def test():

    ###  test parsing a single addresse
    single_s_time = time.time()

    response_single = AddrX.single_parser(url=url, 
                                          address=address[0], 
                                          exclude_address_type=["city"]
                                          )

    print(response_single)

    single_e_time = time.time()

    print("single::: ", single_e_time - single_s_time)

    ####  test parsing list of addresses in synchronously
    sync_s_time = time.time()

    response_sync = AddrX.parser(url=url, 
                                 address_list=addr_list, 
                                 exclude_address_type=["road"]
                                 )

    print(response_sync)

    sync_e_time = time.time()

    print("sync::: ", sync_e_time - sync_s_time)

    ####  test parsing list of addresses in asynchronously
    async_s_time = time.time()

    response_async = AddrX.async_parser(url=url, 
                                        address_list=addr_list, 
                                        exclude_address_type=["road", "country"]
                                        )

    print(response_async)

    async_e_time = time.time()

    print("async::: ", async_e_time - async_s_time)


if __name__ == "__main__":
    test()
