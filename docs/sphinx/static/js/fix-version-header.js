// FIXME: TEMPORARY quick hack to pin the version in header in the "latest" branch

function ready(callback) {
	if (document.readyState !== "loading") {
		callback();
		return;
	}
	document.addEventListener("DOMContentLoaded", callback);
}

ready(() => {
	const rocmHeader = document.querySelector(
		"div.header-logo a[href='https://rocm.docs.amd.com/en/latest']",
	);
	rocmHeader.textContent = "ROCm™ Software 6.2.4"
});
