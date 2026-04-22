# 规范stipulation
# 适用于RCT/ape/libs

APE_DIRS = mbse_core unitizationer mbse_ape mbse_ape_dev model_profile

.PHONY: lock check-lock

# 生成所有RCT系统工程核心包的锁定（静态）文件：
lock:
	@for dir in $(APE_DIRS); do \
		echo "=== 锁定文件： $$dir ==="; \
		(cd $$dir && uv lock); \
	done

# 验证所有锁定文件是否已是最新：
check-lock:
	@for dir in $(APE_DIRS); do \
		echo "=== 验证锁定文件： $$dir ==="; \
		(cd $$dir && uv lock --check) || exit 1; \
	done
