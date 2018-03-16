
from front_base.config import ConfigBase


class Config(ConfigBase):
    def __init__(self, fn):
        super(Config, self).__init__(fn)

        # front
        self.set_var("front_continue_fail_num", 10)
        self.set_var("front_continue_fail_block", 180)

        # http_dispatcher
        self.set_var("dispather_min_idle_workers", 0)
        self.set_var("dispather_work_min_idle_time", 0)
        self.set_var("dispather_work_max_score", 20000)
        self.set_var("dispather_max_workers", 1)
        self.set_var("dispather_score_factor", 100)

        # http 2 worker
        #self.set_var("http2_status_to_close", [])

        # connect_manager
        self.set_var("ssl_first_use_timeout", 5)
        self.set_var("connection_pool_min", 0)
        self.set_var("https_new_connect_num", 0)

        # check_ip
        self.set_var("check_ip_content", "OK")

        # connect_creator
        self.set_var("check_sni", 1)

        # ip_manager
        self.set_var("max_scan_ip_thread_num", 5)
        self.set_var("max_good_ip_num", 100)
        self.set_var("target_handshake_time", 550)

        self.load()