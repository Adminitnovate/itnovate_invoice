from tools.donut.dataset_uploader import DonutDatasetUploader

def main():
    dataset_uploader = DonutDatasetUploader()
    dataset_uploader.upload('docs/models/donut/data', "MADHURIJ/InvoiceData")


fapi = HfApi()

api.upload_folder(
    folder_path="/sparrow-ml",
    repo_id="MADHURIJ/sparrow-ml",
    repo_type="space",
)
if __name__ == '__main__':
    main()